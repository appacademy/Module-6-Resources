# Example Redux State

```javascript
{
   users: {
      1: {
         id: 1,
         username: "Demo",
         email: "demo@aa.io"
      },
   },
   todolists: {
      1: {
         id: 1,
         title: "Chores",
         description: "",
         todo_item_ids: [1, 2, 3, 4]
      },
      2: {
         id: 2,
         title: "Groceries",
         description: "Things I've eaten and need more of",
         todo_item_ids: [5, 6, 7, 8]
      },
   },
   todos: {
      1: {
         id: 1,
         title: "Kitchen counters",
         description: "disinfect and rinse",
         complete: false,
         todolist_id: 1
      },
      2: {
         id: 2,
         title: "Clean toilet",
         description: "disinfect and rinse",
         complete: false,
         todolist_id: 1
      },
      3: {
         id: 3,
         title: "Vacuum living room",
         description: "",
         complete: true,
         todolist_id: 1
      },
      4: {
         id: 4,
         title: "Laundry",
         description: "Wash, Dry, Fold AND put it away, please",
         complete: false,
         todolist_id: 1
      },
      5: {
         id: 5,
         title: "Bananas",
         description: "organic, slightly green",
         complete: false,
         todolist_id: 2
      },
      6: {
         id: 6,
         title: "Eggs",
         description: "",
         complete: false,
         todolist_id: 2
      },
      7: {
         id: 7,
         title: "Bread",
         description: "",
         complete: false,
         todolist_id: 2
      },
      8: {
         id: 8,
         title: "Peanut Butter",
         description: "it better be crunchy",
         complete: false,
         todolist_id: 2
      },
   },
   session: {
      user: {
         id: 1,
         name: 'Demo'
      }
   },
   errors: [
         "Unauthorized",
         "Incorrect username/password combination",
         "Title cannot exceed 20 characters in length"
      ]
}
```
