# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: DailySprint
def dry_run(operation, args, *, store=None):
    """Имитирует операцию над данными без реального изменения."""
    state = store if store is not None else {}
    if operation == "create":
        state.setdefault("projects", {})[args["project"]] = args
    elif operation == "update":
        if "projects" not in state:
            state["projects"] = {}
        state["projects"][args["project"]] = {**state["projects"].get(args["project"], {}), **args}
    elif operation == "delete":
        state["projects"].pop(args["project"], None)
    elif operation == "create_task":
        state.setdefault("tasks", {}).setdefault(args["project"], []).append(args["task"])
    elif operation == "update_task":
        if "tasks" not in state:
            state["tasks"] = {}
        if "project" in args and "task" in args:
            state["tasks"][args["project"]].append(args["task"])
    elif operation == "delete_task":
        if "tasks" not in state:
            state["tasks"] = {}
        if "project" in args:
            state["tasks"][args["project"]] = [t for t in state["tasks"][args["project"]] if t != args["task"]]
    elif operation == "create_focus":
        state.setdefault("focuses", {}).setdefault(args["project"], []).append(args["focus"])
    elif operation == "update_focus":
        if "focuses" not in state:
            state["focuses"] = {}
        if "project" in args and "focus" in args:
            state["focuses"][args["project"]].append(args["focus"])
    elif operation == "delete_focus":
        if "focuses" not in state:
            state["focuses"] = {}
        if "project" in args:
            state["focuses"][args["project"]] = [f for f in state["focuses"][args["project"]] if f != args["focus"]]
    elif operation == "create_retro":
        state.setdefault("retros", []).append(args["retro"])
    elif operation == "update_retro":
        if "retros" not in state:
            state["retros"] = []
        if "retro" in args:
            state["retros"][-1] = {**state["retros"][-1], **args["retro"]}
    elif operation == "delete_retro":
        state["retros"].pop(-1, None)
    return dict(state)
