from textnode import TextType, TextNode 


def main():
    new_node = TextNode("This is some arnchor text", TextType.LINK, "https://www.boot.dev")
    print(new_node)


main()