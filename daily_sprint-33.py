# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: DailySprint
# Undo support for the last action in DailySprint
_last_action = None
_undo_stack = []

def record_action(action):
    """Record a completed action to enable undo."""
    global _last_action
    if _last_action is not None:
        _undo_stack.append(_last_action)
    _last_action = action.copy()

def undo():
    """Revert the most recent recorded action. Returns True if an undo occurred, False otherwise."""
    global _last_action
    if not _undo_stack:
        return False
    previous_state = _undo_stack.pop()
    current_state = _last_action
    _last_action = None  # clear after successful undo
    
    # Apply the inverse of the last action using stored state
    if isinstance(current_state, dict) and "action_type" in current_state:
        action_type = current_state["action_type"]
        
        if action_type == "add_focus":
            focus_id = current_state.get("focus_id")
            # Remove the focus from the list
            new_focuses = [f for f in all_focuses if f["id"] != focus_id]
            all_focuses[:] = new_focuses
            return True
            
        elif action_type == "add_task":
            task_id = current_state.get("task_id")
            # Remove the task from its list
            owner = current_state.get("owner", "daily_sprint")
            if owner in daily_sprints:
                sprint = daily_sprints[owner]
                new_tasks = [t for t in sprint["tasks"] if t["id"] != task_id]
                sprint["tasks"][:] = new_tasks
                return True
                
        elif action_type == "update_task":
            task_id = current_state.get("task_id")
            old_status = current_state.get("old_status", "")
            # Restore the previous status
            if task_id in daily_sprints:
                sprint = daily_sprints[task_id]
                for t in sprint["tasks"]:
                    if t["id"] == task_id and "status" in t:
                        t["status"] = old_status
                        return True
                        
        elif action_type == "delete_task":
            task_id = current_state.get("task_id")
            # Re-add the deleted task with its original data
            deleted_data = current_state.get("deleted_data", {})
            if task_id in daily_sprints:
                sprint = daily_sprints[task_id]
                new_tasks = [t for t in sprint["tasks"] if t["id"] != task_id]
                # Re-add the task with restored data
                new_tasks.append(deleted_data)
                sprint["tasks"][:] = new_tasks
                return True
                
    return False

def can_undo():
    """Check if there is an action available to undo."""
    return _last_action is not None and len(_undo_stack) > 0
