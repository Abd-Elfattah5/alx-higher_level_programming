#include "lists.h"
/**
 * insert_node - function to insert a node in a sorted linked list
 * Return: the address of the new node or NULL if it fails
 * @head: the start of the linked list
 * @number: the number to put in the node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp_new, *temp;

	if (head == NULL)
		return (NULL);
	temp_new = malloc(sizeof(listint_t));

	if (temp_new == NULL)
		return (NULL);
	temp = *head;
	temp_new->n = number;

	if (temp == NULL)
	{
		*head = temp_new;
		return (temp_new);
	}

	while (temp != NULL)
	{
		if (temp->n > temp_new->n)
		{
			temp_new->next = temp;
			*head = temp_new;
			return (temp_new);
		}
		else if (temp->n <= temp_new->n && temp->next == NULL)
		{
			temp->next = temp_new;
			temp_new->next = NULL;
			return (temp_new);
		}
		else if (temp->n <= temp_new->n && temp->next->n >= temp_new->n)
		{
			temp_new->next = temp->next;
			temp->next = temp_new;
			return (temp_new);
		}
		temp = temp->next;
	}
	return (NULL);
}
