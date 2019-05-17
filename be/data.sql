use edu;
insert into CourseGroup
values
    (1, 'IT·互联网');
insert into CourseGroup
values
    (2, '升学·考研');
insert into CourseGroup
values
    (3, '英语·留学');
insert into CourseVariety
values
    (1, '小学', 2);
insert into CourseVariety
values
    (2, '初中', 2);
insert into CourseVariety
values
    (3, '高中', 2);
insert into CourseVariety
values
    (4, '考研', 2);
insert into TeacherInfo
values(1, '15001960017', 'xx教育', '超强阵容，助您上名校', 0);
insert into CourseInfo
value(1,
'中学数学初一上',
'这个是数学课，初一上',
'支持随到随学，报名后两年有效',
10.00,
1,
0,
0,
63072000,
'//10.url.cn/qqcourse_logo_ng/ajNVdqHZLLD5vibyEjkzEQeoB4ZwcOR7mdcRzm7t5oYjxWrJJWd53zgc320P1xBHGsmzcibdNGeLE/356'
);
insert into CourseInfo
value(2,
'高中数学高二下',
'这个是数学课，高二下',
'支持随到随学，报名后两年有效',
10.00,
1,
0,
0,
63072000,
'//10.url.cn/qqcourse_logo_ng/ajNVdqHZLLDMGsJnfqGxILP9iacUpfp6jhs8pS6bwaQgJqdGSNQoSlYMogcJUnphK0E11X7H5ibIg/356'
);
insert into CourseInfo
value(3,
'高考语文解读',
'这个是语文课，为了高考做准备',
'通过讲一些专题课里比较基础的知识，比如现代文的速读课，古诗的如何读懂一首诗，作文的素材积累等',
15.00,
1,
0,
0,
63072000,
'//10.url.cn/qqcourse_logo_ng/ajNVdqHZLLBwOrhoT1KiaOerwB0zjXuzBUN8gHXsNCu3ZwasLJf88fT62wmPKOj6ygHgJwqj2CW8/356?tp=webp'
);
insert into CourseInfo
value(4,
'英语完形填空',
'这个是英语课，为了高考做准备',
'高考英语完形高频词-形容词系列',
99.00,
1,
0,
0,
63072000,
'//10.url.cn/qqcourse_logo_ng/ajNVdqHZLLB5icpricsdpNlBVTLy3iahrmeicbMLUgRDzV33QicDrwSSCzHUVX10k374Y19UFRg5LkNA/356?tp=webp'
);
insert into CourseClassify
values
    (1, 1, 2);
insert into CourseClassify
values
    (2, 2, 3);
insert into CourseClassify
values
    (3, 3, 3);
insert into CourseClassify
values
    (4, 4, 3);
insert into ConnectType values(1, 'QQ群');
insert into ConnectType values(2, '微信号');
insert into ConnectType values(3, '手机号');
insert into TeacherConnect values(1, 1, 1, '1270512112');
insert into TeacherConnect values(2, 2, 1, 'moyui');
insert into TagVariety values(1, '数学');
insert into TagVariety values(2, '名师');
insert into TagVariety values(3, '免费咨询');
insert into CourseTag values(1, 1, 1);
insert into CourseTag values(2, 1, 2);
insert into CourseTag values(3, 2, 1);
insert into CourseTag values(4, 2, 3);
insert into CourseTime values (1, 1, '1552827600');
insert into CourseTime values (2, 2, '1552874400');
insert into CourseMenu values (1, 1, '实数');
insert into CourseMenu values (2, 1, '平面直角坐标系');
insert into CourseMenu values (3, 2, '立体几何');
insert into CourseMenu values (4, 2, '三角函数');
insert into OrderStatus values (1, '已下单，等待付款');
insert into OrderStatus values (2, '已支付完成');
insert into OrderStatus values (3, '等待退款中');
insert into OrderStatus values (4, '已退款');
insert into OrderStatus values (5, '已过期');
insert into VideoInfo values(1, '1020', '立体几何垂直证明技巧', 'https://apd-videohy.apdcdn.tc.qq.com/vedu.tc.qq.com/AviyarfxLYU_LFDOdWR6i4qOTgvQgGv0bkN0dUBkqEAo/t1430ficvkk.p701.1.mp4?sdtfrom=v1101&guid=c0ea33e168cbd67da4958d197d96ec3f&vkey=8DF52AE7F6BDB810BF510B8CBB5A51F696CAE8CB1E4D0276C2D5ACB336947FEE15E53BC0B653C6184E27F9E87F6EC50D6F9890BBEF4080EC3A193D491544CEE9A2730497F5FD7BD0654ED5BA958204DA73337D68DDC3A29DCDB071B7853878D8D4C4BFD12CC93818BBD8BE51CB83CFA2&ocid=531981065', '', 2, 3);
insert into VideoInfo values(2, '1620', '三角函数基本概念', 'https://apd-34ae6fe0c0bf6afc625cd8a10eb5f214.v.smtcdns.com/vedu.tc.qq.com/A9EDe-kmsE7-NAxpSwwDPVwjY6Xok_jakpIxB-W-QbNs/e14222tdfcz.p701.1.mp4?sdtfrom=v1101&guid=c0ea33e168cbd67da4958d197d96ec3f&vkey=FCE62DB51103C367F65EA6C5B1D5D4ABEBF75B8A00E6CD0EF70F9B1E354FCD004CBE542CFAFDE2FDD6C2BAA3A0E800B64A34B36F76EF48BA1E8E608E37F87DA4F73C05A38CE8A262411E56A268A53A1923FF321E5E3524DB61A506809D6DDAEF68E7FBC150318FB43A05F968DC8FB605', '', 2, 4);
insert into VideoInfo values(3, '1920', '球体与截面', 'https://apd-9ace46fc8af4584ef6e351ca4db59a22.v.smtcdns.com/vedu.tc.qq.com/Aj5f-KK_ekFHCzzCR6Od02hTDMqkpnsJppHNFafcUifE/i141601wvlh.p701.1.mp4?sdtfrom=v1101&guid=c0ea33e168cbd67da4958d197d96ec3f&vkey=F0EA0BD7F1FC9F1064B9FC00D2203FD9ED7DBE09AE924400532C1A66865E7E1BC1CE9852E349B6EBCB1EB553D466B5ACD4A5056E2F153CD41B88A1D4713C82ECB0E4D30EA09AA533FEACF857CE30F253A373A49296FD906576304A66918083C1FC513909BD0BCA34F6BD61F0DD2E7607', '', 2, 3);
insert into CommentStatus values(1, '正常');
insert into CommentStatus values(2, '封禁');
insert into PayWay values(1, '支付宝');
insert into PayWay values(2, '微信支付');
insert into PayWay values(3, '课程分销');
insert into PayWay values(4, '课程扣款');
insert into PayWay values(5, '课程退款');
insert into TestType values(-1, '期末考试');
insert into TestType values(1, '平时测试');
insert into CourseTest values(1, '问题1&问题2&问题3', '1;A_B_C&2;&2;', 'A;30&B;30&C;40', 2, -1, -1);
insert into HonerType values(1, '期末成就')