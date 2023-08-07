#include "lists.h"
/**
 * check_cycle - checks if a single linked list has a cycle
 * Return: 0 if there is no cycle, 1 if there is a cycle
 * @list: the head of the linked list
*/
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);

	temp = list->next;

	while (temp != NULL)
	{
		if (temp == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
