def dfs(graph):
    # Track visited nodes
    visited = set()
    # Track nodes to visit (stack)
    stack = []
    
    # Helper to add smallest unvisited node
    def add_smallest_unvisited():
        # Handle empty graph
        if not graph:
            return
        
        # Get all possible nodes (0 to max node in graph)
        all_nodes = set(range(min(graph.keys()), max(graph.keys()) + 1))
        # Find unvisited nodes
        unvisited = all_nodes - visited
        if unvisited:
            stack.append(min(unvisited))
    
    # Start with smallest node
    add_smallest_unvisited()
    
    while stack:
        # Pop from end (stack)
        node = stack.pop()
        
        if node not in visited:
            print(node)
            visited.add(node)
            # Add neighbors in order they appear
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                stack.append(neighbor)
                
        # If we've run out of nodes in stack but haven't visited all nodes
        if not stack:
            add_smallest_unvisited()

def bfs(graph):
    # Track visited nodes
    visited = set()
    # Track nodes to visit (queue)
    queue = []
    
    # Helper to add smallest unvisited node
    def add_smallest_unvisited():
        # Handle empty graph
        if not graph:
            return
            
        # Get all possible nodes (min to max node in graph)
        all_nodes = set(range(min(graph.keys()), max(graph.keys()) + 1))
        # Find unvisited nodes
        unvisited = all_nodes - visited
        if unvisited:
            queue.append(min(unvisited))
    
    # Start with smallest node
    add_smallest_unvisited()
    
    while queue:
        # Pop from start (queue)
        node = queue.pop(0)
        
        if node not in visited:
            print(node)
            visited.add(node)
            # Add neighbors in order they appear
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                queue.append(neighbor)
                
        # If we've run out of nodes in queue but haven't visited all nodes
        if not queue:
            add_smallest_unvisited()