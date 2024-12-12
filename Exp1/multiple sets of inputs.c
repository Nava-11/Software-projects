#include <stdio.h>
#include <math.h>

void calculate_roots(double a, double b, double c) {
    double discriminant = b * b - 4 * a * c;

    switch ((a == 0) ? 3 : (discriminant > 0) ? 1 : (discriminant == 0) ? 2 : 0) {
        case 1: {
            double root1 = (-b + sqrt(discriminant)) / (2 * a);
            double root2 = (-b - sqrt(discriminant)) / (2 * a);
            printf("The roots are: %.2f and %.2f\n", root1, root2);
            break;
        }
        case 2: {
            double root = -b / (2 * a);
            printf("The repeated root is: %.2f\n", root);
            break;
        }
        case 0:
            printf("No real roots.\n");
            break;
        case 3:
            printf("Invalid coefficients (a cannot be zero).\n");
            break;
        default:
            printf("Unexpected case.\n");
    }
}

int main() {
    int choice;
    double a, b, c;

    printf("Select the equation type:\n");
    printf("1. Case 1: a = 2, b = 5, c = 3\n");
    printf("2. Case 2: a = 1, b = -4, c = 4\n");
    printf("3. Case 3: a = 0, b = 1, c = -2 (Invalid quadratic)\n");
    printf("4. Case 4: Custom coefficients\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            a = 1;
            b = 0;
            c = -4;
            printf("\nCase 1 selected: a=%.2f, b=%.2f, c=%.2f\n", a, b, c);
            break;
        case 2:
            a = 1;
            b = -4;
            c = 4;
            printf("\nCase 2 selected: a=%.2f, b=%.2f, c=%.2f\n", a, b, c);
            break;
        case 3:
            a = 0;
            b = 1;
            c = -2;
            printf("\nCase 3 selected: a=%.2f, b=%.2f, c=%.2f\n", a, b, c);
            break;
        case 4:
            printf("\nEnter custom coefficients a, b, c: ");
            scanf("%lf %lf %lf", &a, &b, &c);
            break;
        default:
            printf("Invalid choice.\n");
            return 1;
    }
    calculate_roots(a, b, c);

    return 0;
}
