export const numberToMoney = (number: string, currency: string = 'COP'): string => {
  if (currency === 'COP') {
    return `$${parseFloat(number).toFixed(0)}`
  }
  if (currency !== 'COP') {
    return `$${parseFloat(number).toFixed(0)}`
  }
  return ''
}

export const scrollToId = (id: string) => {
  const element = document.getElementById(id)
  element?.scrollIntoView({behavior: 'smooth'})
}
