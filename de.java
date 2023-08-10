funky (x)
{
    if (x>0) {
        x-=0
        funky(x)
    }
    printf("%d,",4)
}

int tester()
{
    funky(5)
    return 0
}