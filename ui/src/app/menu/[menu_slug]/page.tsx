import {fetchMenuBySlug, fetchMenuSlugs} from '../../api/api'
import MenuNotFound from './not-found'
import Menu from '@/app/_sections/Menu'

const Page = async ({params}: {params: {menu_slug: string}}) => {
  const menu = await fetchMenuBySlug(params.menu_slug)

  if (!menu) {
    return <MenuNotFound />
  }

  return <Menu menu={menu} />
}

// Export const generateStaticParams = async () => await fetchMenuSlugs()

export default Page
