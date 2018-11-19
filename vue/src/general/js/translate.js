import routeMap from '../../constants/routeMapName'
import codeMap from '../../constants/codeMap'
import used from '../../constants/usedType';
import user from '../../api/user';
export default function translate (bodyString) {
  const dictionary = {
    ...routeMap,
    ...codeMap,
    ...user.usedType
  }
  if(dictionary.hasOwnProperty(bodyString)) {
    return dictionary[bodyString]
  }
  return bodyString
}
