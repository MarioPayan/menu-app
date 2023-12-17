// export const dynamic = 'force-dynamic'

import {menus} from '../../data'

export async function GET(request: Request, {params}: {params: {slug: string}}) {
  const slug = params.slug
  const menu = menus.find(menu => menu.slug === slug)

  return Response.json({menu})
}
