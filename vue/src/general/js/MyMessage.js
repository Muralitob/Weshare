import { Message, Notice } from 'iview'
import translate from './translate'
class myMessage {
  constructor(code =0, msg='') {
    this.code = code;
    this.msg = msg;
  }
  successnotice() {
    Notice.success({
      title: translate(this.code),
      desc: this.msg
    });
  }
  errornotice() {
    Message.error(translate(this.code));
  }
}
export default myMessage