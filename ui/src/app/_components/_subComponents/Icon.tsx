import Image from 'next/image'

const defaultIcon = '', // TODO: Add default dish image
  Icon = ({obj, status = "normal"}: {obj: any, status?: "favorite" | "excluded" | "normal"}) => {
    const styles = {
      favorite: {
        border: '1px solid #000',
        filter: 'invert()'
      },
      excluded: {
        opacity: 0.5,
        filter: 'grayscale(100%)'
      },
      normal: {}
    }

    return (
      // <Image src={obj.icon ?? defaultIcon} alt={obj.name ?? "TODO: Add name"} width={32} height={32} />
      <Image
        src='/pizza.png'
        alt='Pizza'
        width={32}
        height={32}
        style={styles[status]}
      />
    )
  }
export default Icon
