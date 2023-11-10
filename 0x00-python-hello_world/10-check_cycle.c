#include "lists.h"

/**
 * check_cycle - a function that checks if the liked
 * list has a cycle
 *
 * list: the head of the list
 *
 * Description - We will navigate the list with 2
 * pointers.
 * One pointer moves to each node in the list (slow)
 * Another moves at twice the pace (fast)
 * If there is a cycle, then eventually fast will
 * catch up to slow
 * If there is no cycle then fast will reach the end of
 * the list (tail) and the pointer to the next node here
 * will be NULL, indicating end of the list and thus
 * no cycle
 *
 * Return: 1 if there is a cycle or else 0
 */

int check_cycle(listint_t *list)
{
	lintint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			free(slow);
			free(fast);
			return 1;
		}

	}
	
	free(slow);
	free(fast);
	return 0;
}
