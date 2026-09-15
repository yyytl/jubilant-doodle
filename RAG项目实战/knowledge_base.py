import hashlib
import os
from webbrowser import Chrome
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_text_splitters import  RecursiveCharacterTextSplitter

def check_md5(md5_str:str):
   """"检查传入的md5是否已经被处理过了"""
   if not os.path.exists(config.md5_path):
      open(config.md5_path,'w',encoding="utf-8").close()
      return False
   else :
      for line in open(config.md5_path,'r',encoding="utf-8").readlines() :
          line=line.strip()    #处理字符串前后空格和回车
          if line==md5_str:
              return True  #已处理过
      return False


def save_md5(md5_str:str):
    """"将传入的md5字符串，记录到文件内保存"""
    with open(config.md5_path,'a',encoding="utf-8") as f:   #a为追加
         f.write(md5_str +"\n")

def get_string_md5(input_str:str,encoding="utf-8"):
    """"将传入的字符串转换为md5字符串"""

    #将字符串转换为bytes字节数组
    str_bytes=input_str.encode(encoding=encoding)

    #创建md5对象
    md5_obj=hashlib.md5()          #得到md5对象
    md5_obj.update(str_bytes)      #更新内容（传入即将要转换的字节数组）
    md5_hex=md5_obj.hexdigest()    #得到md5的十六进制字符串

    return md5_hex


class KnowledgeBaseService(object):
    def __init__(self):
        #如果文件夹不存在就创建，如果存在就跳过
        os.makedirs(config.persist_directory,exist_ok=True)
        self.chroma = Chrome(
            collection_name=config.collection_name,    #数据库的表名
            emdedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory,     #数据库本地存储文件夹
        )      #向量存储的实例Chroma向量库对象
        self.spliter=None     #文本分割器的对象


    def upload_by_str(self,data,filename):
         """"将传入的字符串进行向量化，存入向量数据库中"""
    pass


if __name__ == '__main__':