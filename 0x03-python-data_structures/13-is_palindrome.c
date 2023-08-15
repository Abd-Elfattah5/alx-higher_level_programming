#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * Return: 1 if true , 0 otherwise
 * @head: the head of the linked list
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int list_len = 0, i, j, *values;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp != NULL)
	{
		list_len += 1;
		temp = temp->next;
	}
	temp = *head;
	values = malloc(list_len * sizeof(int));
	for (i = 0; i < list_len; i++)
	{
		values[i] = temp->n;
		temp = temp->next;
	}
	i = 0;
	j = list_len - 1;
	while (i != j && i < j)
	{
		if (values[i] != values[j])
			return (0);
		i++;
		j--;
	}
	free(values);
	return (1);

}
