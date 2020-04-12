from covid import Covid 
import time

covid = Covid()
data = covid.get_data()
agora = time.time()
for pais in data:
    taxa = pais['deaths'] / pais['confirmed'] * 100
    # if taxa > 10:
    #     print('%-40s %3.0f' % (pais['country'], taxa))
    ultima_data = pais['last_update'] / 1000
    if agora - ultima_data >  12 * 60 * 60:
        print(pais['country'], time.ctime(ultima_data))
    # print(ultima_data)
    # print(time.time())
    # print(time.gmtime(ultima_data / 1000))
    # break

