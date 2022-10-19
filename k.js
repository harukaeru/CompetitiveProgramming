p = '👋🏻'
const unicodeSubstring = (str, start, end) => {
  const reg = new RegExp(`^.{${start}}(.{0,${end - start}})`, 'u')
  console.log('reg', reg)
  return str.match(reg)?.[1]
}

console.log(unicodeSubstring(p, 0, 2))
