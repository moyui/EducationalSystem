import Vue from 'vue';
import {
  Button,
  Container,
  Footer,
  Header,
  Menu,
  Aside,
  Submenu,
  MenuItem,
  Card,
  Form,
  FormItem,
  Input,
  Main,
  Popover,
  Dialog,
  Notification,
  Message,
  TabPane,
  Tabs,
  Breadcrumb,
  BreadcrumbItem,
  Table,
  TableColumn,
  Row,
  Col,
  Tag,
  Rate,
  Alert,
  Radio,
  RadioGroup,
  Divider
} from 'element-ui';

Vue.use(Button);
Vue.use(Container);
Vue.use(Footer);
Vue.use(Header);
Vue.use(Menu);
Vue.use(Aside);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Submenu);
Vue.use(MenuItem);
Vue.use(Card);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Input);
Vue.use(Main);
Vue.use(Popover);
Vue.use(Dialog);
Vue.use(TabPane);
Vue.use(Tabs);
Vue.use(Breadcrumb);
Vue.use(BreadcrumbItem);
Vue.use(Row);
Vue.use(Col);
Vue.use(Tag);
Vue.use(Rate);
Vue.use(Alert);
Vue.use(Radio);
Vue.use(RadioGroup);
Vue.use(Divider);

Vue.prototype.$notify = Notification;
Vue.prototype.$message = Message;
