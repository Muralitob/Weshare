//统一管理iview组件
import Vue from 'vue';
import { Button, 
         BackTop, 
         Dropdown, 
         DropdownMenu, 
         DropdownItem, 
         Icon, 
         Row, 
         Col, 
         Input, 
         Avatar, 
         Menu, 
         MenuItem, 
         Card, 
         MenuGroup,
         Message,
         Checkbox,
         Spin,
         Notice,
         Upload,
         Tabs,
         TabPane,
         Page,
         Affix,
         Divider,
         Carousel,
         CarouselItem,
         } from 'iview';
Vue.prototype.$Message = Message
Vue.prototype.$Notice = Notice

Vue.component('Button', Button);
Vue.component('Icon', Icon);
Vue.component('Row', Row);
Vue.component('Col', Col);
Vue.component('Input', Input);
Vue.component('Avatar', Avatar);
Vue.component('Menu', Menu);
Vue.component('MenuItem', MenuItem);
Vue.component('Card', Card);
Vue.component('BackTop', BackTop);
Vue.component('MenuGroup', MenuGroup);
Vue.component('Dropdown', Dropdown);
Vue.component('DropdownItem', DropdownItem);
Vue.component('Checkbox', Checkbox);
Vue.component('DropdownMenu', DropdownMenu);
Vue.component('Spin', Spin);
Vue.component('Upload', Upload);
Vue.component('Tabs', Tabs);
Vue.component('TabPane', TabPane);
Vue.component('Page', Page)
Vue.component('Affix', Affix)
Vue.component('Divider', Divider)
Vue.component('Carousel', Carousel)
Vue.component('CarouselItem', CarouselItem)
