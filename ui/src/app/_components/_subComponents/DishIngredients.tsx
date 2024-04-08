import Icon from './Icon'

const DishIngredients = ({ ingredients, ingredientsPreferences }: any) => {
  const getIconStatus = (ingredient: any) => {
    if (ingredientsPreferences.isFavorite(ingredient.id)) {
      return 'favorite'
    }
    if (ingredientsPreferences.isExcluded(ingredient.id)) {
      return 'excluded'
    }
    return 'normal'
  }
  return (
    <>
      {ingredients.map((ingredient: any) => (
        <Icon
          key={ingredient.id}
          obj={ingredient}
          status={getIconStatus(ingredient)}
        />
      ))}
    </>
  )
}

export default DishIngredients
