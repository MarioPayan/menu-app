const API_URL = 'http://localhost:8000',
  ENDPOINTS = {
    menuSlugs: 'api/menu-slug',
    menus: 'menus',
  },
  menuSlugsEnpoint = (): string => `${API_URL}/${ENDPOINTS.menuSlugs}`,
  menuBySlugEnpoint = (slug: string): string => `${API_URL}/${ENDPOINTS.menus}/${slug}?expanded=True&random=True`

interface FetchMenuSlugs {
  (): Promise<string[]>
}

interface FetchMenuBySlug {
  (slug: string): Promise<any | undefined>
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
  try {
    return await fetch(menuBySlugEnpoint(slug)).then(res => res.json())
  } catch (error) {
    console.error(error) // TODO: handle error
  }
}
