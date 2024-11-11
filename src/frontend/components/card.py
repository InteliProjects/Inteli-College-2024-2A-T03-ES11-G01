from streamlit_extras.stylable_container import stylable_container


def card_container(key=None):
    return stylable_container(key=key, css_styles=[
        """
        {
            --tw-ring-offset-shadow: 0 0 #0000;
            --tw-ring-shadow: 0 0 #0000;
            --tw-shadow: 0 1px 3px 0 rgba(0,0,0,.1),0 1px 2px -1px rgba(0,0,0,.1);
            border-radius: 4px; 
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
            # transition: 0.2s; /* Smooth transition for hover effect */
            padding: 1.5em; /* Inner spacing */
            border: 1px solid #e5e7eb;
            box-sizing: border-box;
            background-color: #FFFFFF; 
            box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
            color: black;
            margin: 0;
            display: flex;
            flex-wrap: wrap; /* Allow content to wrap within the container */
            max-width: 100%; /* Ensure the content does not exceed 100% width */
            min-width: 0; /* Prevent min-width from being too large */
        }
        """,
        """
        > div:not(:first-child) {
            width: 100%;
            min-width: 1px;
            flex: 1 1 auto;
            display: flex;
        }
        """,
        # """
        # > div:first-child {
        #     display: none;
        # }
        # """,
        """
        > div:not(:first-child) > iframe {
            display: flex;
            width: 100%; /* Adjusting for padding */
            min-width: 1px;
            border: none;
        }
        """,
        """
        > div:not(:first-child) canvas {
            display: flex;
            width: 100% !important; /* Adjusting for padding */
            min-width: 1px;
            border: none;
            flex: 1 1 auto;
        }
        """,
        """
        > .h3 {
            color: black;
        }
        """
    ])