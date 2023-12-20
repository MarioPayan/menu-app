import {fetchMenuSlugs} from './api/api'
import styles from './page.module.css'

export default async function Home() {
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
