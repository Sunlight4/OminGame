import os
import urllib2
import shutil
import math

download_list=[]
def downloadChunks(url):

    """Helper to download large files

        the only arg is a url
       this file will go to a temp directory

       the file will also be downloaded

       in chunks and print out how much remains
    """
    global download_list
    baseFile = os.path.basename(url)

 
    #move the file to a more uniq path

    os.umask(0002)

    temp_path = os.getcwd()

    try:

        f = baseFile
        if os.path.exists(f):
            print baseFile, "already exists"
            return f

 
        req = urllib2.urlopen(url)

        total_size = int(req.info().getheader('Content-Length').strip())

        downloaded = 0

        CHUNK = 256 * 10240

        with open(f, 'wb') as fp:

            while True:

                chunk = req.read(CHUNK)

                downloaded += len(chunk)

                print math.floor( (downloaded / total_size) * 100 )

                if not chunk: break

                fp.write(chunk)
            download_list.append(f)

    except urllib2.HTTPError, e:

        print "HTTP Error:",e.code , url

        return False

    except urllib2.URLError, e:

        print "URL Error:",e.reason , url

        return False

    print download_list 
    return f

def get_resource_path(name, domain):
    url="http://vsurvival.com/SMBG-resources/"+domain+"/"+name
    r=downloadChunks(url)
    print r
    return r
def done():
    for i in download_list:
        os.unlink(i)
        print "deleted", i
    
    
    
