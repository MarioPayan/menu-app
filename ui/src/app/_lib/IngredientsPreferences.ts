class IngredientsPreferences {
  favorites: Set<string> = new Set()
  excluded: Set<string> = new Set()

  constructor(favorites: Set<string> = new Set(), excluded: Set<string> = new Set()) {
    this.favorites = favorites
    this.excluded = excluded
  }

  getUpdated() {
    return new IngredientsPreferences(new Set(this.favorites), new Set(this.excluded))
  }

  isFavorite(ingredientId: string) {
    return this.favorites.has(ingredientId)
  }

  isExcluded(ingredientId: string) {
    return this.excluded.has(ingredientId)
  }

  isNone(ingredientId: string) {
    return !this.isFavorite(ingredientId) && !this.isExcluded(ingredientId)
  }

  setFavorite(ingredientId: string) {
    this.favorites.add(ingredientId)
    this.excluded.delete(ingredientId)
    return this.getUpdated()
  }

  setExcluded(ingredientId: string) {
    this.excluded.add(ingredientId)
    this.favorites.delete(ingredientId)
    return this.getUpdated()
  }

  setNormal(ingredientId: string) {
    this.excluded.delete(ingredientId)
    this.favorites.delete(ingredientId)
    return this.getUpdated()
  }

  cyclePreference(ingredientId: string) {
    if (this.isNone(ingredientId)) {
      this.setFavorite(ingredientId)
    } else if (this.isFavorite(ingredientId)) {
      this.setExcluded(ingredientId)
    } else if (this.isExcluded(ingredientId)) {
      this.setNormal(ingredientId)
    }
    return this.getUpdated()
  }
}

export default IngredientsPreferences
