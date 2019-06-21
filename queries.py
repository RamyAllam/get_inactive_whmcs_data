inactive_clients_query = "select id, firstname, lastname, email, address1, city, state, country from tblclients" \
                        " where (status='Inactive')"  \
                        " AND (email NOT LIKE '%@gmail.%')"  \
                        " AND (email NOT LIKE '%@googlemail.%')"  \
                        " AND (email NOT LIKE '%@yahoo.%')"  \
                        " AND (email NOT LIKE '%@live.%')"  \
                        " AND (email NOT LIKE '%@aol.%')"  \
                        " AND (email NOT LIKE '%@hotmail.%')"  \
                        " AND (email NOT LIKE '%@outlook.%')"  \
                        " AND (email NOT LIKE '%@msn.%')"  \
                        " AND (email NOT LIKE '%@qq.%')" \
                        " AND (email NOT LIKE '%@yandex.%')" \
                        " AND (email NOT LIKE '%@me.%')" \
                        " AND (email NOT LIKE '%@mail.%')" \
                        " AND (email NOT LIKE '%@icloud.%')"
