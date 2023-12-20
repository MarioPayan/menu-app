// export const dynamic = 'force-dynamic'

import {menus} from '../data'

export async function GET(request: Request) {
  console.log(request)
  const slugs = menus.map(menu => menu.slug)

  return Response.json({slugs})
}
