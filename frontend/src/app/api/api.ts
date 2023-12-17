const API_URL = 'http://localhost:3000'
const ENDPOINTS = {
  menuSlugs: 'api/menu-slug',
  menu: 'api/menu',
}

const menuSlugsEnpoint = (): string => `${API_URL}/${ENDPOINTS.menuSlugs}`
const menuBySlugEnpoint = (slug: string): string => `${API_URL}/${ENDPOINTS.menu}/${slug}`

interface FetchMenuSlugs {
  (): Promise<string[]>
}

interface FetchMenuBySlug {
  (slug: string): Promise<Menu | undefined>
}

export const fetchMenuSlugs: FetchMenuSlugs = async () => {
  let result = []
  try {
    const data = await fetch(menuSlugsEnpoint()).then(res => res.json())
    result = data.slugs
  } catch (error) {
    console.error(error) // TODO: handle error
  }
  return result
}

export const fetchMenuBySlug: FetchMenuBySlug = async slug => {
  let result = undefined
  try {
    const data = await fetch(menuBySlugEnpoint(slug)).then(res => res.json())
    result = data.menu
  } catch (error) {
    console.error(error) // TODO: handle error
  }
  return result
}
