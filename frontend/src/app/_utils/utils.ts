export const numberToMoney = (number: number = 0, currency: string = 'COP') => {
  if (currency === 'COP') return `$${number.toFixed(0)}`
}

export const numberToPercentage = (number: number = 0) => `%${Math.round(number)}`
