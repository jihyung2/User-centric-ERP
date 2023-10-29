from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
import datetime
import time
import pymysql


class PEx(BehaviorModelExecutor):

  def __init__(self, instance_time, destruct_time, name, engine_name):
    BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name,
                                   engine_name)
    self.init_state("Wait")
    self.insert_state("Wait", Infinite)
    # self.insert_state("Generate", 1)
    self.insert_state("rest", 1)
    self.insert_state("bal_a", 1)
    self.insert_state("saeng_jang", 1)
    self.insert_state("chul_su", 1)
    self.insert_state("sung_suk", 1)
    self.insert_input_port("start")
    # self.custom_date = ''

  def ext_trans(self, port, msg):
    if port == "start":
      # print(f"[app started]")
      # print("Date input : ")
      # date_ = input()
      # self.set_date(date_)
      self._cur_state = "bal_a"

# edited by 최준혁 / 이혜림

  def output(self):
    self.index = 0
    self.item_list = [] 
    print("==========================")
    for i in range(len(self.menu)):
      self._cur_state, self.temp = self.int_trans()
      if self.temp == "empty": #만약 데이터안에 없는 품목이라면 적정 온도 출력을 생략하고 다음 품목으로 넘어감
        print(f"{self.menu[self.index]}이 데이터 상에 없습니다.\n")
        self.index += 1
        continue
      # print("[%s][%s]: %s"%(self.menu[self.index], self._cur_state,datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
      # print("[%s][%s] : %s"%(self.menu[self.index],self._cur_state, self.get_date()))
      #품목과 상태를 출력
      # print(f"적정온도 : {self.temp}\n")
      # print(f"{self.temp}") 
      # # 온도 출력하는 부분

      self.item_list.append(int(self.temp))
      self.index += 1

    print(self.item_list)
    self.put_db(self.item_list)
    self.item_list = []
    time.sleep(5)
    self.index = 0
    return None

  def put_db(self, item_list) :
    db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',port=3306)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("UPDATE simulation SET rice = %s, banana = %s, casava = %s", item_list)
    db.commit()


  def int_trans(self):
    cur_time = datetime.datetime.now().strftime("%m-%d")
    # date_data = self.get_date()
    # data_format = "%m-%d"
    # cur_time = datetime.datetime.strptime(date_data, data_format)
    # cur_time = datetime.datetime.strftime(cur_time, data_format)
    if self.menu[self.index] == "rice":
      if cur_time <= "02-01":
        return "rest", 0 
        
      elif cur_time <= "03-01":
        return "bal_a", 10  #현 상태와 적정 온도를 같이 리턴
  
      elif cur_time <= "06-01":
        return "saeng_jang", 20
  
      elif cur_time <= "09-01":
        return "chul_su", 30
  
      elif cur_time <= "12-01":
        return "sung_suk", 15

      elif cur_time <= "12-31":
        return "rest", 0
        
    if self.menu[self.index] == "banana":
      if cur_time <= "04-30":
        return "rest", 18
        
      elif cur_time <= "10-01":
        return "saeng_yuk", 27
  
      elif cur_time <= "12-31":
        return "rest", 18

    if self.menu[self.index] == "cassava":
      if cur_time <= "04-30":
        return "rest", 0
      
      elif cur_time <= "11-15":
        return "saeng_jang", 15
      
      elif cur_time <= "12-31":
        return "rest", 0

    return self._cur_state, "empty"

  def insert_list(self, arr):
    setattr(self, "menu", arr)
    setattr(self, "index", 0)
    setattr(self, "temp", 0)

  # def set_date(self, date_) :
  #   self.custom_date = date_
  
  # def get_date(self) :
  #   return self.custom_date

def start():
  menu = ['rice', 'banana', 'cassava'] #이 곳에 GUI에서 농사하고 있는 품목들을 받아오면 됨
  ss = SystemSimulator()
  ss.register_engine("first", "REAL_TIME", 1)
  ss.get_engine("first").insert_input_port("start")
  gen = PEx(0, Infinite, "Gen", "first")
  gen.insert_list(menu)
  ss.get_engine("first").register_entity(gen)
  ss.get_engine("first").coupling_relation(None, "start", gen, "start")
  ss.get_engine("first").insert_external_event("start", None)
  ss.get_engine("first").simulate()

start()