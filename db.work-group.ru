$TTL    604800
@       IN      SOA     work-group.ru. root.work-group.ru. (
                      2         ; Serial
                 604800         ; Refresh
                  86400         ; Retry
                2419200         ; Expire
                 604800 )       ; Negative Cache TTL
;
        IN      NS      work-group.ru.
        IN      A       192.168.0.2  ; IP-адрес вашего DNS-сервер
two     IN      A       192.168.1.2
one     IN      A       192.168.0.2
