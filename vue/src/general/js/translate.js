import routeMap from '../../constants/routeMapName'
export function translate (bodyString) {
  const dictionary = {
    ...routeMap,
  }
  if(dictionary.hasOwnProperty(bodyString)) {
    return dictionary[bodyString]
  }
  return bodyString
}