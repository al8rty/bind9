$TTL    604800
@       IN      SOA     work-group.ru. root.work-group.ru. (
                      2         ; Serial
                 604800         ; Refresh
                  86400         ; Retry
                2419200         ; Expire
                 604800 )       ; Negative Cache TTL
;
        IN      NS      work-group.ru.
        IN      A       192.168.100.2  ; IP-адрес вашего DNS-сервера
hq-rtr  IN      A       192.168.100.1
br-rtr  IN      A       192.168.200.1
hq-srv  IN 	A	192.168.100.2
hq-cli	IN	A	192.168.100.66
br-srv	IN	A	192.168.200.2
moodle	IN	hq-rtr.work-group.ru.
wiki	IN	hq-rtr.work-group.ru.