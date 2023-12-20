import {fetchMenuSlugs} from './api/api'
import styles from './page.module.css'

export default async function Home() {
  // TODO: url should looks like www.app.com/<restaurant-slug>/<menu-slug> and www.app.com/<restaurant-slug>/admin
  const slugs = await fetchMenuSlugs()
  return (
    <main className={styles.main}>
      {slugs.map(slug => (
        <a href={`http://localhost:3000/menu/${slug}`} key={slug}>
          {slug}
        </a>
      ))}
    </main>
  )
}
