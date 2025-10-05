create table user_favorite
(
  user_id int not null,
  product_id int not null
);

insert into user_favorite values (1,1);
insert into user_favorite values (1,2);
insert into user_favorite values (1,3);
insert into user_favorite values (3,1);
insert into user_favorite values (3,2);
insert into user_favorite values (3,3);
