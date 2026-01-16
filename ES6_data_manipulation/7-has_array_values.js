export default function setFromArray(set, array) {
  return array.every(element => set.has(element));
}
