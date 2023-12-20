// export const dynamic = 'force-dynamic'

import {menus} from '../data'

export async function GET(request: Request) {
  const slugs = menus.map(menu => menu.slug)

  return Response.json({slugs})
}
