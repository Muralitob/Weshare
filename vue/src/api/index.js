import user from './user';
import article from './article'
import good from './good'
import talk from './talk'
export default {
  ...user,
  ...article,
  ...good,
  ...talk,
}
