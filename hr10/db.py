import pymysql

class Hr10Info(object):
    def __init__(self,tableName):
        self.tableName = tableName

    # mysql数据库链接设置
    def add_hr10(self,job_name,detail_link,public_data,location,people_num,job_type,content):
        db = pymysql.Connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "123",
            db = "spider",
            charset = "utf8"

        )
        cursor = db.cursor()
        # 插入内容的sql语句
        sql = "insert into %s(job_name,detail_link,public_data,location,people_num,job_type,content) value('%s','%s','%s','%s','%s','%s','%s')"%(self.tableName,job_name,detail_link,public_data,location,people_num,job_type,content)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

    def get_count(self):
        db = pymysql.Connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "123",
            db = "spider",
            charset = "utf8"

        )
        cursor = db.cursor()
        sql = "select count(1) from %s"%(self.tableName)
        cursor.execute(sql)
        total_count = cursor.fetchone()
        cursor.close()
        db.close()
        return total_count

    def outinfo(self,keyword,city,job_type,begin,total):
        result = {}
        config = {
            'host':"localhost",
            'port':3306,
            'user':"root",
            'passwd':"123",
            'db':'spider',
            'charset':'utf8',
            'cursorclass':pymysql.cursors.DictCursor
        }
        db = pymysql.Connect(**config)
        cursor = db.cursor()
        # 用于查询输出内容的sql语句
        sql = "select * from %s where (job_name like '%%%s%%' or content like '%%%s%%') and location='%s' and job_type='%s' limit %s,%s"%(self.tableName,keyword,keyword,city,job_type,begin,total)
        print(sql)
        items = []
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # 遍历返回的结果 并将所有内容一个个压入items字典中
            for row in result:
                item = {}
                item["job_name"] = row["job_name"]
                item["detail_link"] = row["detail_link"]
                item["content"] = row["content"]
                item["public_data"] = row["public_data"]
                item["location"] = row["location"]
                item["people_num"] = row["people_num"]
                item["job_type"] = row["job_type"]
                items.append(item)

        except:
            pass
        finally:
            cursor.close()
            db.close()
        return items
    

    def create_table(self,tableName):
        db = pymysql.Connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "123",
            db = "spider",
            charset = "utf8"

        )
        cursor = db.cursor()
        # mysql数据库中判断是否已经创建了表 若没有 则在此创建
        sql = """
        CREATE TABLE IF NOT EXISTS `""" +self.tableName+ """`  (
        `Id` int(11) NOT NULL AUTO_INCREMENT,
        `job_name` varchar(255) DEFAULT NULL,
        `detail_link` varchar(255) DEFAULT NULL,
        `public_data` varchar(255) DEFAULT NULL,
        `location` varchar(255) DEFAULT NULL,
        `people_num` varchar(255) DEFAULT NULL,
        `job_type` varchar(255) DEFAULT NULL,
        `content` text,
        PRIMARY KEY (`Id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        """
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
                



# # '''
hr10 = Hr10Info("hrinfo10")

hr10.create_table("hrinfo10")


# hr10.add_hr10("ddd","sdfsfd","sdfffff","ddd","sdfsfd","sdfffff","qqqq")
# hr10.add_hr10("ddd","sdfsfd","sdfffff","ddd","sdfsfd","sdfffff","qqqq")
# hr10.add_hr10("ddd","sdfsfd","sdfffff","ddd","sdfsfd","sdfffff","qqqq")
# hr10.add_hr10("ddd","sdfsfd","sdfffff","ddd","sdfsfd","sdfffff","qqqq")
# print(hr10.get_count())
# print(hr10.outinfo(2,7))
# # '''

