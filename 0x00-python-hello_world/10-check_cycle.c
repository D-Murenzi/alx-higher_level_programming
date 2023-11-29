/* this program checks if a list have a circle in it*/
#include <stdio.h>

/**
 * check_cycle-function to check for cycle in linked list
 * @list: the pointer to the list
 * Return: 0 when no cycle or 1 on cycled list
 */

int check_cycle(listint_t *list)
{
	if (list)
	{
		listint_t *ptr0, *ptr1;

		ptr0 = list;
		ptr1 = list;

		while (ptr1 != NULL)
		{
			ptr1 = ptr1->next;
			if (ptr1 == ptr0)
			{
				return (1);
			}
		}
	}
	return (0);
}
