#coding=utf-8

import pymysql.cursors

config = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'wangruidong',
    'db':'danmu',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}

class Mysql(object):
    def __init__(self):
        self.connection = pymysql.connect(**config)

    def __del__(self):
        self.connection.close()


    def isDanmuExist(self, rowId):
        '''
        rowId is the primary key in danmu offical database.
        :param rowId:
        :return:
        '''
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM bili_danmu WHERE bd_rowId = (%s)"
                cursor.execute(sql,(rowId))
                result = cursor.fetchone()
                if result == None :
                    return False
                else:
                    return True
            self.connection.commit()
        finally:
            pass
    def insertAvNumber(self,av_number):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO tmp(av_number) VALUES (%s)"
                cursor.execute(sql,(av_number) )
            self.connection.commit()
        except Exception as e:
            print(e)

    def insertDanmu(self, av_number,video_num,danmu,time_in_video,type,size,color,time_post,pool,user_num,rowId, isCheck=False):
        '''
        If the video is exist, then check danmu.
        :param fieldDic:
        :param isCheck: Check danmu whether exist
        :return:
        '''
        if ( isCheck ) :
            if self.isDanmuExist(rowId):
                print(' Danmu already exist.')
                return
        try:
            with self.connection.cursor() as cursor :

                # danmu 表
                # sql = "INSERT INTO danmu(av_number,time_in_video,time_post,danmu) VALUES(%s,%s,%s,%s)"
                # cursor.execute(sql,(av_number,time_in_video,time_post,danmu))

                # bili_danmu 表
                sql = "INSERT INTO bili_danmu(bd_av_number," \
                      "bd_video_num," \
                      "bd_danmu," \
                      "bd_time_in_video," \
                      "bd_type," \
                      "bd_size," \
                      "bd_color," \
                      "bd_time_post," \
                      "bd_pool," \
                      "bd_user_num," \
                      "bd_rowId) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(av_number,video_num,danmu,time_in_video,
                                    type,size,color,time_post,pool,user_num,rowId))

            self.connection.commit()
        except Exception as e:
            print(' Exception occur in insertDanmu , rowId = ',rowId)
            print(e)


    def isVideoExist(self,av_number,cid):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM bili_video where bv_av_number = (%s) AND bv_cid = (%s)"
                cursor.execute(sql,(av_number,cid))
                result = cursor.fetchone()
                if result == None :
                    return False
                else :
                    return True
        finally:
            pass

    def insertVideo(self, av_number, video_num, url, tags, classify, title, date, description, danmu_sum, cid):
        if ( self.isVideoExist(av_number, cid ) ) :
            print('bili video alrady exist av_number = ', av_number,' video_num = ', video_num)
            return
        else:
            try:
                print('Insert a video, av_number = ', av_number,' number = ', video_num)
                with self.connection.cursor() as cursor :
                    print("Insert a bili video "+av_number)
                    sql = "INSERT INTO bili_video(bv_av_number," \
                          " bv_video_num," \
                          " bv_url," \
                          " bv_tags, " \
                          "bv_classify," \
                          "bv_title," \
                          "bv_date," \
                          "bv_description," \
                          "bv_danmu_sum, " \
                          "bv_cid ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (av_number, video_num, url, tags, classify, title, date, description, danmu_sum, cid))
                self.connection.commit()
            except Exception as e:
                print('Error insert a video, av_number = ', av_number,' video_num = ', video_num)
                print(e)

    def queryDanmu(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM danmu"
                cursor.execute(sql)
                result = cursor.fetchone()
                out_file = open('data.txt','w')
                for val in result.keys():
                    print(val)
                    print(result[val])
                    out_file.write(result[val])
                out_file.close()
                print("query success")
            self.connection.commit()
        finally:
            pass

    def getNextVideoNumber(self, av_number,cid):
        if (self.isVideoExist(av_number,cid) == True ):
            return 1;
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * from bili_video WHERE bv_av_number=(%s)"
                cursor.execute(sql,(av_number))
                result = cursor.fetchall()
                if ( result == None or len(result) == 0 ):
                    return 1
                else:
                    return len(result) + 1
            self.connection.commit()
        finally:
            pass
    def getVideoNumer(self, av_number):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * from bili_video WHERE bv_av_number=(%s)"
                cursor.execute(sql,(av_number))
                result = cursor.fetchall()
                if ( result == None or len(result) == 0 ):
                    return 0
                else:
                    return len(result)
            self.connection.commit()
        finally:
            pass

    def updateVideoDanmuNumber(self, av_number, video_num, danmu_sum):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE bili_video set bv_danmu_sum = (%s) WHERE bv_av_number=(%s) AND bv_video_num=(%s)"
                cursor.execute(sql, (danmu_sum, av_number, video_num))
            self.connection.commit()
        finally:
            pass

    def queryVideo(self, av_number):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT COUNT(*) FROM video WHERE av_number=(%s)"
                cursor.execute(sql,(av_number))
                result = cursor
            self.connection.commit()
            if not result:
                return True
            else:
                return False
        finally:
            pass

    def fixbug(self):
        try:
            with self.connection.cursor() as cursor:
                sql1 = "SELECT bv_av_number,bv_video_num FROM bili_video"
                cursor.execute(sql1)
                result = cursor.fetchall()
                print(len(result))
                for ele in result:
                    sql2 = "SELECT * FROM bili_danmu WHERE bd_av_number=(%s) AND bd_video_num=(%s)"
                    cursor.execute(sql2,(ele['bv_av_number'],ele['bv_video_num']))
                    ret2 = cursor.fetchall()
                    danmu_num = len(ret2)
                    print('danmu_num = ',danmu_num)
                    self.updateVideoDanmuNumber(av_number=ele['bv_av_number'],video_num=ele['bv_video_num'],danmu_sum=danmu_num)
        finally:
            pass



if __name__ == '__main__':
    my = Mysql()
    my.fixbug()
