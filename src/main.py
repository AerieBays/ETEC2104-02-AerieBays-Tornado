import asyncio
import os, os.path
import tornado.web
import Index
import Templates.ProfileTemplate as ProfileTemplate
import csv
import glob

HTMLDIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..", "html"
                 )
)

def makeApp():
    endpoints=[]
    with open("src/users.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if os.path.getsize(f'temp/{row["username"]}temp') == 0:
                    keepgoing = True
                else:
                    keepgoing = False
            except:
                keepgoing = True
            with open(f'temp/{row["username"]}temp', 'a') as newcsv:
                if keepgoing:
                    writer = csv.DictWriter(newcsv, fieldnames=row.keys(), lineterminator='\n')
                    writer.writeheader()
                    writer.writerow(row)
                endpoints.append((f'/profile/{row["username"]}', ProfileTemplate.Handler, ))
                newcsv.close()
            endpoints.append(("/", Index.Handler))  # new

    app = tornado.web.Application(endpoints,
                                  static_path=HTMLDIR
                                  )
    app.listen(8000)
    return app

if __name__ == "__main__":
    files = glob.glob('temp/*')
    for f in files:
        os.remove(f)
    makeApp()
    asyncio.get_event_loop().run_forever()