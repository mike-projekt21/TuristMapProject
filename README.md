# Навигационная система по достопримечательностям.
Это навигационное приложение для платформы Android, позволяющее пользователю не только прокладывать пешеходные маршруты для прогулок по городу, но и получать подробную информацию о туристических местах и достопримечательностях города.

## Концепция
-    Наш навигатор будет показывать на карте города достопримечательности так, что пользователям приложения не придется искать нужные места среди множества магазинов, остановок общественного транспорта и т.д.
-    Пользователь может найти и ознакомится с информацией по интересующему его объекту;
-    Приложение будет прокладывать пешеходный маршрут так, чтобы пользователь мог пройти мимо ближайших достопримечательностей.
  
  Проект написан на *Kivy.Framework* для Python, вёрстка экранов сделана с помощью отдельных .kv файлов на языке *Kivy Design Language*
При запуске приложения пользователь попадает на основной экран с картой. В нижней части экрана находится Tab Bar с помощью которого осуществляется навигация по приложению. Три иконки отвечают за три основных экрана: основной экран, экран поиска и экран профиля.

  Далее идёт экран работы с профилем, на котором отображается основная информация пользователя. В случае если пользователь не авторизирован, открываются формы входа в уже созданный аккаунт или регистрации нового. 
В профиле можно посмотреть статистику и выйти из аккаунта. Во вкладке "статистика" можно увидеть все места, в которых вы побывали во время пользования приложением, посмотреть достопримечательности, посещенные вами недавно, и увидеть свой список любимых мест.
 
  На экране поиска можно найти конкретную достопримечательность или проложить маршрут. Выбрав конкретную достопримечательность открывается страница достопримечательности. На ней можно видеть фото и описание выбранного культурного объекта. Также, нажав на сердечко, можно добавить достопримечательность в список любимых. Исторические и культурные памятники, которые чаще всего добавляют в любимые будут показываться в списке популярных, что позволит находить места для посещения, которые больше всего нравятся другим пользователям.

  Для работы с картой пришлось интегрировать виджет *MapView* из дополнительной библиотеки к Kivy – *kivy_garden*. 
(Первоначально мы нашли  и хотели использовать открытый API Open Street Maps (OSM). Однако, изучив документацию kivy_garden было обнаружено, что она как раз базируется на OSM. С её помощью можно использовать весь необходимый функционал OSM. Он позволил нам решить вопрос по работе с геолокацией, расставлением меток на карте по координатам построек, и проложение маршрутов между точками.)

## На данный момент
- имеется отрисованный GUI основных экранов. Между ними налажена навигация при помощи ToolBarа. 
- функционирует регистрация пользователя и работа с аккаунтом,
- функционирует просмотр информации о достопримечательностях,
- функционирует проложение оптимального маршрута
