const menu6: Menu = {
  id: 1,
  created_at: '2023-01-01',
  modified_at: '2023-01-02',
  slug: 'paninos',
  name: 'Italian Delights',
  restaurant: {
    id: 1,
    created_at: '2023-01-01',
    modified_at: '2023-01-02',
    name: 'Pasta Paradise',
    slug: 'pasta-paradise',
    description: 'Authentic Italian Cuisine',
    banner: 'https://via.placeholder.com/800x200',
    icon: 'https://via.placeholder.com/50x50',
  },
  dishes: [
    {
      id: 1,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Spaghetti Bolognese',
      prices: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          size: 'Regular',
          originalPrice: 32900,
          discountPercentage: 10,
          finalPrice: 29000,
          currency: 'COP',
        },
      ],
      description: 'Classic Italian pasta with rich meat sauce and parmesan cheese',
      categories: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Pasta',
          description: 'Italian pasta dishes',
        },
        {
          id: 2,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Meat Lovers',
          description: 'Dishes for meat enthusiasts',
        },
      ],
      ingredients: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Ground Beef',
          description: 'High-quality ground beef',
          categories: [
            {
              id: 1,
              created_at: '2023-01-01',
              modified_at: '2023-01-02',
              name: 'Meat',
              description: 'Main meat ingredients',
            },
          ],
        },
        {
          id: 2,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Tomato Sauce',
          description: 'Freshly made tomato sauce',
          categories: [
            {id: 3, created_at: '2023-01-01', modified_at: '2023-01-02', name: 'Sauces', description: 'Savory sauces'},
          ],
        },
      ],
      mainImage: '/assets/images/dish1.png',
      images: ['https://via.placeholder.com/200x150'],
      recommended: true,
    },
    {
      id: 1,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Spaghetti Bolognese',
      prices: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          size: 'Regular',
          originalPrice: 32900,
          discountPercentage: 10,
          finalPrice: 29000,
          currency: 'COP',
        },
      ],
      description: 'Classic Italian pasta with rich meat sauce and parmesan cheese',
      categories: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Pasta',
          description: 'Italian pasta dishes',
        },
        {
          id: 2,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Meat Lovers',
          description: 'Dishes for meat enthusiasts',
        },
      ],
      ingredients: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Ground Beef',
          description: 'High-quality ground beef',
          categories: [
            {
              id: 1,
              created_at: '2023-01-01',
              modified_at: '2023-01-02',
              name: 'Meat',
              description: 'Main meat ingredients',
            },
          ],
        },
        {
          id: 2,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Tomato Sauce',
          description: 'Freshly made tomato sauce',
          categories: [
            {id: 3, created_at: '2023-01-01', modified_at: '2023-01-02', name: 'Sauces', description: 'Savory sauces'},
          ],
        },
      ],
      mainImage: '/assets/images/dish1.png',
      images: ['https://via.placeholder.com/200x150'],
      recommended: true,
    },
  ],
  categories: [
    {id: 1, created_at: '2023-01-01', modified_at: '2023-01-02', name: 'Pasta', description: 'Italian pasta dishes'},
    {
      id: 2,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Meat Lovers',
      description: 'Dishes for meat enthusiasts',
    },
    {
      id: 3,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Vegetarian',
      description: 'Delicious vegetarian options',
    },
  ],
  ingredients: [
    {
      id: 1,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Ground Beef',
      description: 'High-quality ground beef',
      categories: [
        {
          id: 1,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Meat',
          description: 'Main meat ingredients',
        },
      ],
    },
    {
      id: 2,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Tomato Sauce',
      description: 'Freshly made tomato sauce',
      categories: [
        {id: 3, created_at: '2023-01-01', modified_at: '2023-01-02', name: 'Sauces', description: 'Savory sauces'},
      ],
    },
    {
      id: 3,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Parmesan Cheese',
      description: 'Grated parmesan cheese',
      categories: [
        {id: 4, created_at: '2023-01-01', modified_at: '2023-01-02', name: 'Cheese', description: 'Variety of cheeses'},
      ],
    },
    // Add more ingredients as needed
  ],
  combos: [
    {
      id: 1,
      created_at: '2023-01-01',
      modified_at: '2023-01-02',
      name: 'Family Pasta Feast',
      description: 'A feast for the whole family',
      image: 'https://via.placeholder.com/400x300',
      dishes: [
        {
          id: 2,
          created_at: '2023-01-01',
          modified_at: '2023-01-02',
          name: 'Lasagna',
          prices: [{id: 2, created_at: '2023-01-01', modified_at: '2023-01-02', size: 'Regular', price: 20}],
          description: 'Layers of pasta, rich meat sauce, and melted cheese',
          categories: [
            {
              id: 1,
              created_at: '2023-01-01',
              modified_at: '2023-01-02',
              name: 'Pasta',
              description: 'Italian pasta dishes',
            },
            {
              id: 2,
              created_at: '2023-01-01',
              modified_at: '2023-01-02',
              name: 'Cheesy Delights',
              description: 'Dishes with extra cheese',
            },
          ],
          ingredients: [
            {
              id: 2,
              created_at: '2023-01-01',
              modified_at: '2023-01-02',
              name: 'Ricotta Cheese',
              description: 'Smooth and creamy ricotta cheese',
              categories: [
                {
                  id: 2,
                  created_at: '2023-01-01',
                  modified_at: '2023-01-02',
                  name: 'Cheese',
                  description: 'Dairy and cheese ingredients',
                },
              ],
            },
            {
              id: 3,
              created_at: '2023-01-01',
              modified_at: '2023-01-02',
              name: 'Mozzarella Cheese',
              description: 'Fresh mozzarella cheese',
              categories: [
                {
                  id: 4,
                  created_at: '2023-01-01',
                  modified_at: '2023-01-02',
                  name: 'Cheese',
                  description: 'Variety of cheeses',
                },
              ],
            },
            // Add more ingredients as needed
          ],
          mainImage: 'https://via.placeholder.com/400x300',
          images: ['https://via.placeholder.com/200x150'],
          recommended: false,
        },
        // Add more dishes as needed
      ],
      price: {id: 3, created_at: '2023-01-01', modified_at: '2023-01-02', size: 'Family', price: 50},
    },
    // Add more combos as needed
  ],
}

const menus: Menu[] = [menu6]

export {menus}
