import routeMap from '../../constants/routeMapName'
import codeMap from '../../constants/codeMap'
export function translate (bodyString) {
  const dictionary = {
    ...routeMap,
    ...codeMap,
  }
  if(dictionary.hasOwnProperty(bodyString)) {
    return dictionary[bodyString]
  }
  return bodyString
}