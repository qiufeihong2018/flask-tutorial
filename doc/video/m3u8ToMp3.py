#!/usr/bin/python3
 
# In[1]:
 
 
import requests
import re
 
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
 
 
# In[2]:
 
 
headers = {
    'User-Agent': ua,
}
 
response = requests.get('https://apd-20bfccf79577cbf5fc861c7da5c5d233.v.smtcdns.com/sportsts.tc.qq.com/A7OVJhvEBJpI5ZmTkVYUrxyrM2SF83XARGvcVFrWbF8A/uwMROfz2r5zEIaQXGdGnC2df644gnVUys-UbswKsczcTHIZa/LzaMxQBfTbeblJw7Gyi06kG6RrYK1_nQspj83QXyzn5qJi9DBfxdJDXGGQ0RsXHGYV1osm00MPdKMB_fR8YY6NdDlNKtXQ-sRWh_x7TuAHVLq-Ovw0PtT6FL58lnZ92oul3fCsc0L9ultNBILtgygHeM9-2RhkVt2VXpV0LZ730/h0033bbrzkd.321002.ts.m3u8?ver=4', headers=headers)
 
 
# In[6]:
 
 
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://v.qq.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'User-Agent': ua,
    'Accept': '*/*',
    'Referer': 'https://v.qq.com/x/page/d0019qdukl5.html',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
}
 
 
# In[8]:
 
 
result = re.findall(r'^\d+.*index=\d+.*$', response.text, re.M)
 
 
# In[10]:
 
 
fmp4 = open('0.mp4', 'wb')
for i,r in enumerate(result):
    # print(i)
    # print(r)
    print(i, end=', ', flush=True)   # 进度
    rsp = requests.get('https://apd-20bfccf79577cbf5fc861c7da5c5d233.v.smtcdns.com/sportsts.tc.qq.com/A7OVJhvEBJpI5ZmTkVYUrxyrM2SF83XARGvcVFrWbF8A/uwMROfz2r5zEIaQXGdGnC2df644gnVUys-UbswKsczcTHIZa/LzaMxQBfTbeblJw7Gyi06kG6RrYK1_nQspj83QXyzn5qJi9DBfxdJDXGGQ0RsXHGYV1osm00MPdKMB_fR8YY6NdDlNKtXQ-sRWh_x7TuAHVLq-Ovw0PtT6FL58lnZ92oul3fCsc0L9ultNBILtgygHeM9-2RhkVt2VXpV0LZ730/h0033bbrzkd.321002.ts.m3u8?ver=4'+r, headers=headers)
    fmp4.write(rsp.content)
    f = open('{0:0>8}.ts'.format(i), 'wb')
    f.write(rsp.content)
    f.close()
fmp4.close()